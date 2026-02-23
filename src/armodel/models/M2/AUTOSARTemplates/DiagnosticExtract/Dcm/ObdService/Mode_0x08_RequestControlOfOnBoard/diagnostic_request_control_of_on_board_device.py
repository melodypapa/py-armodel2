"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_control_ref: Optional[Any]
    test_id_identifier_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control_ref: Optional[Any] = None
        self.test_id_identifier_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestControlOfOnBoardDevice to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestControlOfOnBoardDevice, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request_control_ref
        if self.request_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.request_control_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize test_id_identifier_ref
        if self.test_id_identifier_ref is not None:
            serialized = SerializationHelper.serialize_item(self.test_id_identifier_ref, "DiagnosticTestRoutineIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEST-ID-IDENTIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDevice":
        """Deserialize XML element to DiagnosticRequestControlOfOnBoardDevice object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestControlOfOnBoardDevice object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestControlOfOnBoardDevice, cls).deserialize(element)

        # Parse request_control_ref
        child = SerializationHelper.find_child_element(element, "REQUEST-CONTROL-REF")
        if child is not None:
            request_control_ref_value = ARRef.deserialize(child)
            obj.request_control_ref = request_control_ref_value

        # Parse test_id_identifier_ref
        child = SerializationHelper.find_child_element(element, "TEST-ID-IDENTIFIER-REF")
        if child is not None:
            test_id_identifier_ref_value = ARRef.deserialize(child)
            obj.test_id_identifier_ref = test_id_identifier_ref_value

        return obj



class DiagnosticRequestControlOfOnBoardDeviceBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticRequestControlOfOnBoardDevice with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRequestControlOfOnBoardDevice = DiagnosticRequestControlOfOnBoardDevice()


    def with_request_control(self, value: Optional[any (DiagnosticRequest)]) -> "DiagnosticRequestControlOfOnBoardDeviceBuilder":
        """Set request_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_control = value
        return self

    def with_test_id_identifier(self, value: Optional[DiagnosticTestRoutineIdentifier]) -> "DiagnosticRequestControlOfOnBoardDeviceBuilder":
        """Set test_id_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.test_id_identifier = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticRequestControlOfOnBoardDevice:
        """Build and return the DiagnosticRequestControlOfOnBoardDevice instance with validation."""
        self._validate_instance()
        pass
        return self._obj