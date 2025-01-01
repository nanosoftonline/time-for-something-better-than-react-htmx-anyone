from flask import Blueprint, request, render_template, redirect
from use_cases.get_products import get_products_from_db

router = Blueprint('products', __name__, url_prefix="/products")


@router.route("/", methods=["GET"])
def get_products():
       products = get_products_from_db()
       return render_template("product/list.html", products=products)
