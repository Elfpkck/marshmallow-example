from dataclasses import dataclass
from typing import Dict

import marshmallow as ma
import marshmallow_dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from base_app import Doc


class DocSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Doc
        include_fk = True


class DocQueryArgsSchema(ma.Schema):
    id = ma.fields.Integer()
    type = ma.fields.String()


@dataclass
class Custom:
    foo: int
    bar: str


CustomSchema = marshmallow_dataclass.class_schema(Custom)

if __name__ == '__main__':
    # without dataclass

    class CustomSchema(ma.Schema):
        foo = ma.fields.Integer()
        baz = ma.fields.DateTime()

        @ma.pre_load
        def validate_input(self, data: Dict, **kwargs):
            data["foo"] = data.get("foo") * 2
            return data

        @ma.post_load
        def secure_data(self, data: Dict, **kwargs):
            return data


    schema = CustomSchema()
    loaded = schema.load({"foo": 42, "baz": "2014-08-17T14:58:57.600623+00:00"})
    print(loaded)
    dumped = schema.dump(loaded)
    print(dumped)
