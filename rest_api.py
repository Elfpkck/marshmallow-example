from flask.views import MethodView
from flask_smorest import Blueprint

from base_app import db
from schemas import Custom, CustomSchema, Doc, DocQueryArgsSchema, DocSchema

blp = Blueprint(
    'docs', 'docs', url_prefix='/docs',
    description='Operations on docs'
)


@blp.route('')
class Docs(MethodView):
    @blp.arguments(DocQueryArgsSchema, location='query', as_kwargs=True)
    @blp.response(DocSchema(many=True))
    def get(self, **kwargs):
        return Doc.query.filter_by(**kwargs).all()

    @blp.arguments(DocSchema)
    @blp.response(DocSchema, code=201)
    def post(self, new_data):
        doc = Doc(**new_data)
        db.session.add(doc)
        db.session.commit()
        return doc


@blp.route('/custom', methods=["POST"])
@blp.arguments(CustomSchema, location='json')
@blp.response(CustomSchema)
def get_custom_data(custom_arg: "Custom"):
    return Custom(foo=custom_arg.foo * 2, bar=custom_arg.bar * 2)
