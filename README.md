# Djackets - E-Commerce Platform

Djackets is a full-featured e-commerce platform built with Django and Vue.js, providing a seamless shopping experience. The platform includes:

- **Stripe Payment Integration**
- **User Authentication and Authorization**
- **Product Catalog and Cart System**
- **Order History in User Profiles**

## Technologies Used

- **Backend:** Django, Django REST Framework, Djoser
- **Frontend:** Vue.js, Bulma, Sass, Axios, Vuex, Bulma Toast
- **Payments:** Stripe
- **Utilities:** Pillow, CORS Headers

---

## Installation and Setup

### Backend Setup

1. Ensure you have Python and `pipenv` installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/milad-2003/djackets/
   cd djackets
   ```
3. Create a virtual environment and activate it:
   ```bash
   pipenv shell
   ```
4. Install dependencies:
   ```bash
   pipenv install
   ```
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
7. Access the admin panel at `http://127.0.0.1:8000/admin` and create two categories: **Summer** and **Winter**. You can also add products in the admin panel.
8. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Ensure you have Node.js installed on your system.
   
2. Navigate to the Vue.js project folder:
   ```bash
   cd djackets_vue
   ```

3. Install the dependencies:
   ```bash
   npm install
   ```

4. Run the development server:
   ```bash
   npm run serve
   ```

---

## Contributing

We welcome contributions to Djackets! Here's how you can contribute:

1. **Fork the repository** to your GitHub account.
2. **Clone your fork** to your local machine:
   ```bash
   git clone <your_forked_repo_url>
   ```
3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b <branch_name>
   ```
4. Make your changes and commit them with descriptive messages:
   ```bash
   git commit -m "Add/Update/Remove <feature_description>"
   ```
5. Push your branch to your fork:
   ```bash
   git push origin <branch_name>
   ```
6. Open a pull request on the main repository and describe your changes.

---

## Notes

- All backend dependencies are managed with `Pipfile` and `Pipfile.lock`.
- All frontend dependencies are managed with `package.json` and `package-lock.json` located in the `djackets_vue` folder.

For any queries or issues, feel free to open an issue in the repository.
