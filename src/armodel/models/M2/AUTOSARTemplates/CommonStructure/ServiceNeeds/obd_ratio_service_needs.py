"""ObdRatioServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 795)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ObdRatioConnectionKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_type: Optional[ObdRatioConnectionKindEnum]
    rate_based_monitored_event_ref: Optional[ARRef]
    used_fid_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ObdRatioServiceNeeds."""
        super().__init__()
        self.connection_type: Optional[ObdRatioConnectionKindEnum] = None
        self.rate_based_monitored_event_ref: Optional[ARRef] = None
        self.used_fid_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdRatioServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdRatioServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_type
        if self.connection_type is not None:
            serialized = SerializationHelper.serialize_item(self.connection_type, "ObdRatioConnectionKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_based_monitored_event_ref
        if self.rate_based_monitored_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rate_based_monitored_event_ref, "DiagnosticEventNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-BASED-MONITORED-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_fid_ref
        if self.used_fid_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_fid_ref, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-FID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioServiceNeeds":
        """Deserialize XML element to ObdRatioServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioServiceNeeds, cls).deserialize(element)

        # Parse connection_type
        child = SerializationHelper.find_child_element(element, "CONNECTION-TYPE")
        if child is not None:
            connection_type_value = ObdRatioConnectionKindEnum.deserialize(child)
            obj.connection_type = connection_type_value

        # Parse rate_based_monitored_event_ref
        child = SerializationHelper.find_child_element(element, "RATE-BASED-MONITORED-EVENT-REF")
        if child is not None:
            rate_based_monitored_event_ref_value = ARRef.deserialize(child)
            obj.rate_based_monitored_event_ref = rate_based_monitored_event_ref_value

        # Parse used_fid_ref
        child = SerializationHelper.find_child_element(element, "USED-FID-REF")
        if child is not None:
            used_fid_ref_value = ARRef.deserialize(child)
            obj.used_fid_ref = used_fid_ref_value

        return obj



class ObdRatioServiceNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for ObdRatioServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ObdRatioServiceNeeds = ObdRatioServiceNeeds()


    def with_connection_type(self, value: Optional[ObdRatioConnectionKindEnum]) -> "ObdRatioServiceNeedsBuilder":
        """Set connection_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connection_type = value
        return self

    def with_rate_based_monitored_event(self, value: Optional[DiagnosticEventNeeds]) -> "ObdRatioServiceNeedsBuilder":
        """Set rate_based_monitored_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rate_based_monitored_event = value
        return self

    def with_used_fid(self, value: Optional[FunctionInhibitionNeeds]) -> "ObdRatioServiceNeedsBuilder":
        """Set used_fid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_fid = value
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


    def build(self) -> ObdRatioServiceNeeds:
        """Build and return the ObdRatioServiceNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj