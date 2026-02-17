"""Unit tests for representative AUTOSAR classes."""

import pytest


class TestRepresentativeClasses:
    """Tests for representative classes from different categories."""

    @pytest.mark.skip(reason="Builder methods with_short_name and with_category not yet implemented")
    def test_sw_base_type_instantiation(self):
        """Test that SwBaseType can be instantiated (SWUT_MODELS_011)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.PrimitiveTypes.sw_base_type import (
            SwBaseType,
            SwBaseTypeBuilder,
        )

        obj = SwBaseTypeBuilder().with_short_name("TestType").with_category(
            "FIXED"
        ).build()

        assert obj is not None
        assert isinstance(obj, SwBaseType)
        assert obj.short_name == "TestType"
        assert obj.category == "FIXED"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_implementation_data_type_instantiation(self):
        """Test that ImplementationDataType can be instantiated (SWUT_MODELS_012)."""
        from armodel.models.M2.AUTOSARTemplates.SwComponentTemplate.Datatype.Datatypes.implementation_data_type import (
            ImplementationDataType,
            ImplementationDataTypeBuilder,
        )

        obj = ImplementationDataTypeBuilder().with_short_name("TestType").build()

        assert obj is not None
        assert isinstance(obj, ImplementationDataType)
        assert obj.short_name == "TestType"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_sw_component_type_instantiation(self):
        """Test that SwComponentType can be instantiated (SWUT_MODELS_013)."""
        from armodel.models.M2.AUTOSARTemplates.SwComponentTemplate.SwComponentTypes.sw_component_type import (
            SwComponentType,
            SwComponentTypeBuilder,
        )

        obj = SwComponentTypeBuilder().with_short_name("TestComponent").build()

        assert obj is not None
        assert isinstance(obj, SwComponentType)
        assert obj.short_name == "TestComponent"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_runnable_entity_instantiation(self):
        """Test that RunnableEntity can be instantiated (SWUT_MODELS_014)."""
        from armodel.models.M2.AUTOSARTemplates.SwComponentTemplate.SwcInternalBehavior.runnable_entity import (
            RunnableEntity,
            RunnableEntityBuilder,
        )

        obj = RunnableEntityBuilder().with_short_name("TestRunnable").build()

        assert obj is not None
        assert isinstance(obj, RunnableEntity)
        assert obj.short_name == "TestRunnable"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_diagnostic_trouble_code_instantiation(self):
        """Test that DiagnosticTroubleCode can be instantiated (SWUT_MODELS_015)."""
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_uds import (
            DiagnosticTroubleCodeUDS,
            DiagnosticTroubleCodeUDSBuilder,
        )

        obj = DiagnosticTroubleCodeUDSBuilder().with_short_name("TestDTC").build()

        assert obj is not None
        assert isinstance(obj, DiagnosticTroubleCodeUDS)
        assert obj.short_name == "TestDTC"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_port_prototype_instantiation(self):
        """Test that PortPrototype can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.SwComponentTemplate.Components.port_prototype import (
            PortPrototype,
            PortPrototypeBuilder,
        )

        obj = PortPrototypeBuilder().with_short_name("TestPort").build()

        assert obj is not None
        assert isinstance(obj, PortPrototype)
        assert obj.short_name == "TestPort"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_referrable_instantiation(self):
        """Test that Referrable can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable.referrable import (
            Referrable,
            ReferrableBuilder,
        )

        obj = ReferrableBuilder().with_short_name("TestReferrable").build()

        assert obj is not None
        assert isinstance(obj, Referrable)
        assert obj.short_name == "TestReferrable"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_compu_method_instantiation(self):
        """Test that CompuMethod can be instantiated."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.CompuMethod.compu_method import (
            CompuMethod,
            CompuMethodBuilder,
        )

        obj = CompuMethodBuilder().with_short_name("TestCompuMethod").build()

        assert obj is not None
        assert isinstance(obj, CompuMethod)
        assert obj.short_name == "TestCompuMethod"