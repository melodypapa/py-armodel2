"""Unit tests for ARObjectBuilder."""


from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
    ARObjectBuilder,
)


class TestARObjectBuilder:
    """Test ARObjectBuilder functionality."""

    def test_builder_init(self):
        """Test builder initialization."""
        builder = ARObjectBuilder()
        assert builder is not None

    def test_builder_build_returns_object(self):
        """Test builder returns ARObject instance."""
        builder = ARObjectBuilder()
        obj = builder.build()

        # Builder returns an instance of ARObject
        assert isinstance(obj, ARObject)
        assert obj is not ARObject  # Not the class itself