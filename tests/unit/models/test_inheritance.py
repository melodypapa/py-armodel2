"""Unit tests for inheritance."""

import pytest


class TestInheritance:
    """Tests for class inheritance and method resolution order."""

    def test_arobject_inheritance(self):
        """Test that classes inherit from ARObject (SWUT_MODELS_400)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

        autosar = AUTOSAR()
        pkg = ARPackage()

        assert isinstance(autosar, ARObject)
        assert isinstance(pkg, ARObject)

    def test_method_resolution_order(self):
        """Test that MRO is correct (SWUT_MODELS_401)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import Referrable

        mro = ARPackage.__mro__
        assert ARObject in mro

        mro = Referrable.__mro__
        assert ARObject in mro

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_xml_member_inheritance(self):
        """Test that XMLMember metadata is inherited (SWUT_MODELS_402)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        # AUTOSAR should inherit ARObject's _xml_members
        assert "checksum" in ARObject._xml_members

        # The serialization framework should collect from entire hierarchy
        autosar = AUTOSAR()
        namespace = "http://autosar.org/schema/r4.0"
        element = autosar.serialize(namespace)

        # Should be able to serialize inherited attributes
        assert element is not None

    def test_referrable_inherits_from_arobject(self):
        """Test that Referrable inherits from ARObject."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import Referrable

        ref = Referrable()
        assert isinstance(ref, ARObject)

    def test_identifiable_inherits_from_referrable(self):
        """Test that Identifiable inherits from Referrable."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import Referrable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import Identifiable

        ident = Identifiable()
        assert isinstance(ident, Referrable)

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_serialize_method_inheritance(self):
        """Test that serialize method is inherited."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

        pkg = ARPackage()
        assert hasattr(pkg, "serialize")
        assert callable(pkg.serialize)

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_deserialize_method_inheritance(self):
        """Test that deserialize method is inherited."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

        assert hasattr(ARPackage, "deserialize")
        assert callable(ARPackage.deserialize)