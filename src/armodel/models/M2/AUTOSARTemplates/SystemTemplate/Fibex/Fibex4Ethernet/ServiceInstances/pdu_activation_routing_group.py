"""PduActivationRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 488)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_group_ref: Optional[EventGroupControlTypeEnum]
    i_pdu_identifier_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[EventGroupControlTypeEnum] = None
        self.i_pdu_identifier_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PduActivationRoutingGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduActivationRoutingGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_group_ref
        if self.event_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_group_ref, "EventGroupControlTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_identifier_refs (list to container "I-PDU-IDENTIFIER-REFS")
        if self.i_pdu_identifier_refs:
            wrapper = ET.Element("I-PDU-IDENTIFIER-REFS")
            for item in self.i_pdu_identifier_refs:
                serialized = SerializationHelper.serialize_item(item, "SoConIPduIdentifier")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-IDENTIFIER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduActivationRoutingGroup":
        """Deserialize XML element to PduActivationRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduActivationRoutingGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduActivationRoutingGroup, cls).deserialize(element)

        # Parse event_group_ref
        child = SerializationHelper.find_child_element(element, "EVENT-GROUP-REF")
        if child is not None:
            event_group_ref_value = ARRef.deserialize(child)
            obj.event_group_ref = event_group_ref_value

        # Parse i_pdu_identifier_refs (list from container "I-PDU-IDENTIFIER-REFS")
        obj.i_pdu_identifier_refs = []
        container = SerializationHelper.find_child_element(element, "I-PDU-IDENTIFIER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_identifier_refs.append(child_value)

        return obj



class PduActivationRoutingGroupBuilder(IdentifiableBuilder):
    """Builder for PduActivationRoutingGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()


    def with_event_group(self, value: Optional[EventGroupControlTypeEnum]) -> "PduActivationRoutingGroupBuilder":
        """Set event_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_group = value
        return self

    def with_i_pdu_identifiers(self, items: list[SoConIPduIdentifier]) -> "PduActivationRoutingGroupBuilder":
        """Set i_pdu_identifiers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = list(items) if items else []
        return self


    def add_i_pdu_identifier(self, item: SoConIPduIdentifier) -> "PduActivationRoutingGroupBuilder":
        """Add a single item to i_pdu_identifiers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers.append(item)
        return self

    def clear_i_pdu_identifiers(self) -> "PduActivationRoutingGroupBuilder":
        """Clear all items from i_pdu_identifiers list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = []
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


    def build(self) -> PduActivationRoutingGroup:
        """Build and return the PduActivationRoutingGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj