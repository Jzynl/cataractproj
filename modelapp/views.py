from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CataractScan, UserProfile
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from django.conf import settings


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('upload')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')


@login_required
def upload_view(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']

        scan = CataractScan.objects.create(
            user=request.user,
            image=image_file,
            diagnosis='unknown',
            confidence=0.0
        )

        try:
            # Paths to model and labels
            model_dir = os.path.join(settings.BASE_DIR, 'model')
            model_path = os.path.join(model_dir, 'model.h5')
            labels_path = os.path.join(model_dir, 'labels.txt')

            # Load model and labels
            model = tf.keras.models.load_model(model_path)
            with open(labels_path, 'r') as f:
                class_labels = [line.strip() for line in f.readlines()]

            # Process image for prediction
            img = Image.open(image_file).convert('RGB')
            img = img.resize((224, 224))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Predict
            prediction = model.predict(img_array)[0]
            predicted_index = np.argmax(prediction)
            confidence = float(prediction[predicted_index])
            predicted_label = class_labels[predicted_index]

            # Save results
            scan.diagnosis = predicted_label
            scan.confidence = confidence
            scan.save()

            return redirect('result', scan_id=scan.id)

        except Exception as e:
            messages.error(request, f'Error processing image: {str(e)}')
            scan.delete()

    return render(request, 'upload.html')


@login_required
def result_view(request, scan_id):
    try:
        scan = CataractScan.objects.get(id=scan_id, user=request.user)
        context = {
            'scan': scan,
            'confidence_percentage': int(scan.confidence * 100)
        }
        return render(request, 'result.html', context)
    except CataractScan.DoesNotExist:
        messages.error(request, 'Scan not found')
        return redirect('upload')


@login_required
def history_view(request):
    scans = CataractScan.objects.filter(user=request.user)
    return render(request, 'history.html', {'scans': scans})


@login_required
def profile_view(request):
    profile, _created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def logout_view(request):
    logout(request)
    return redirect('login')
