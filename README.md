# 🚀 Django REST Framework (DRF) - Concepts & Patterns

This repository is a collection of Django REST Framework implementations, focusing on understanding the **evolution of views**—from basic Function-Based Views to advanced Generic Views.

The goal is to understand *how* DRF works under the hood by implementing the same API logic using different layers of abstraction.

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-5.0+-green?style=flat&logo=django)
![DRF](https://img.shields.io/badge/DRF-Latest-red?style=flat)

## 📚 Concepts Covered

I have implemented CRUD operations using four different approaches to understand the trade-offs between flexibility and code brevity.

### 1. Function Based Views (The Basics)
- Writing raw logic using `@api_view` decorators.
- Manual handling of `GET`, `POST`, `PUT`, `DELETE`.

### 2. Class Based Views (`APIView`)
- Moving from functions to Classes.
- Understanding `get()`, `post()`, `put()`, `delete()` methods within a class.
- Full control over the response logic.

### 3. Mixins & GenericAPIView (The Building Blocks)
Using `GenericAPIView` combined with specific mixins to reuse common logic:
- `ListModelMixin` (Get all)
- `CreateModelMixin` (Post)
- `RetrieveModelMixin` (Get single)
- `UpdateModelMixin` (Put/Patch)
- `DestroyModelMixin` (Delete)

### 4. Concrete Generic Views (The Power House)
Using pre-built views to write APIs in minimal lines of code:
- `ListAPIView`
- `CreateAPIView`
- `RetrieveAPIView`
- `UpdateAPIView`
- `ListCreateAPIView`
- `RetrieveUpdateAPIView`
- `RetrieveDestroyAPIView`
- `RetrieveUpdateDestroyAPIView`

---

## ⚙️ Installation & Setup

If you want to run this locally:

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>