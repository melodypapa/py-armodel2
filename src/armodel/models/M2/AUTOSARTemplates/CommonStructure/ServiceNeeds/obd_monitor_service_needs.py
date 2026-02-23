"""ObdMonitorServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

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
    DiagnosticMonitorUpdateKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdMonitorServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_data_ref: Optional[ARRef]
    event_needs_ref: Optional[ARRef]
    unit_and_scaling_id: Optional[PositiveInteger]
    update_kind: Optional[DiagnosticMonitorUpdateKindEnum]
    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data_ref: Optional[ARRef] = None
        self.event_needs_ref: Optional[ARRef] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdMonitorServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdMonitorServiceNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_data_ref
        if self.application_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.application_data_ref, "ApplicationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_needs_ref
        if self.event_needs_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_needs_ref, "DiagnosticEventNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-NEEDS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_and_scaling_id
        if self.unit_and_scaling_id is not None:
            serialized = SerializationHelper.serialize_item(self.unit_and_scaling_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-AND-SCALING-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update_kind
        if self.update_kind is not None:
            serialized = SerializationHelper.serialize_item(self.update_kind, "DiagnosticMonitorUpdateKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdMonitorServiceNeeds":
        """Deserialize XML element to ObdMonitorServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdMonitorServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdMonitorServiceNeeds, cls).deserialize(element)

        # Parse application_data_ref
        child = SerializationHelper.find_child_element(element, "APPLICATION-DATA-REF")
        if child is not None:
            application_data_ref_value = ARRef.deserialize(child)
            obj.application_data_ref = application_data_ref_value

        # Parse event_needs_ref
        child = SerializationHelper.find_child_element(element, "EVENT-NEEDS-REF")
        if child is not None:
            event_needs_ref_value = ARRef.deserialize(child)
            obj.event_needs_ref = event_needs_ref_value

        # Parse unit_and_scaling_id
        child = SerializationHelper.find_child_element(element, "UNIT-AND-SCALING-ID")
        if child is not None:
            unit_and_scaling_id_value = child.text
            obj.unit_and_scaling_id = unit_and_scaling_id_value

        # Parse update_kind
        child = SerializationHelper.find_child_element(element, "UPDATE-KIND")
        if child is not None:
            update_kind_value = DiagnosticMonitorUpdateKindEnum.deserialize(child)
            obj.update_kind = update_kind_value

        return obj



class ObdMonitorServiceNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for ObdMonitorServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ObdMonitorServiceNeeds = ObdMonitorServiceNeeds()


    def with_application_data(self, value: Optional[ApplicationDataType]) -> "ObdMonitorServiceNeedsBuilder":
        """Set application_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application_data = value
        return self

    def with_event_needs(self, value: Optional[DiagnosticEventNeeds]) -> "ObdMonitorServiceNeedsBuilder":
        """Set event_needs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_needs = value
        return self

    def with_unit_and_scaling_id(self, value: Optional[PositiveInteger]) -> "ObdMonitorServiceNeedsBuilder":
        """Set unit_and_scaling_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit_and_scaling_id = value
        return self

    def with_update_kind(self, value: Optional[DiagnosticMonitorUpdateKindEnum]) -> "ObdMonitorServiceNeedsBuilder":
        """Set update_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.update_kind = value
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


    def build(self) -> ObdMonitorServiceNeeds:
        """Build and return the ObdMonitorServiceNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj