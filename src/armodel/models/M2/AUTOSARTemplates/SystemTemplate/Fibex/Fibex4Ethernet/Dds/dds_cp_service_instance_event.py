"""DdsCpServiceInstanceEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 475)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DdsCpServiceInstanceEvent(ARObject):
    """AUTOSAR DdsCpServiceInstanceEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_event_ref: Optional[ARRef]
    dds_event_qos_ref: Optional[ARRef]
    dds_event_topic_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceEvent."""
        super().__init__()
        self.dds_event_ref: Optional[ARRef] = None
        self.dds_event_qos_ref: Optional[ARRef] = None
        self.dds_event_topic_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpServiceInstanceEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpServiceInstanceEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_event_ref
        if self.dds_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_event_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_event_qos_ref
        if self.dds_event_qos_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_event_qos_ref, "DdsCpQosProfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-EVENT-QOS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_event_topic_ref
        if self.dds_event_topic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_event_topic_ref, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-EVENT-TOPIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstanceEvent":
        """Deserialize XML element to DdsCpServiceInstanceEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpServiceInstanceEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpServiceInstanceEvent, cls).deserialize(element)

        # Parse dds_event_ref
        child = SerializationHelper.find_child_element(element, "DDS-EVENT-REF")
        if child is not None:
            dds_event_ref_value = ARRef.deserialize(child)
            obj.dds_event_ref = dds_event_ref_value

        # Parse dds_event_qos_ref
        child = SerializationHelper.find_child_element(element, "DDS-EVENT-QOS-REF")
        if child is not None:
            dds_event_qos_ref_value = ARRef.deserialize(child)
            obj.dds_event_qos_ref = dds_event_qos_ref_value

        # Parse dds_event_topic_ref
        child = SerializationHelper.find_child_element(element, "DDS-EVENT-TOPIC-REF")
        if child is not None:
            dds_event_topic_ref_value = ARRef.deserialize(child)
            obj.dds_event_topic_ref = dds_event_topic_ref_value

        return obj



class DdsCpServiceInstanceEventBuilder(BuilderBase):
    """Builder for DdsCpServiceInstanceEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpServiceInstanceEvent = DdsCpServiceInstanceEvent()


    def with_dds_event(self, value: Optional[PduTriggering]) -> "DdsCpServiceInstanceEventBuilder":
        """Set dds_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_event = value
        return self

    def with_dds_event_qos(self, value: Optional[DdsCpQosProfile]) -> "DdsCpServiceInstanceEventBuilder":
        """Set dds_event_qos attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_event_qos = value
        return self

    def with_dds_event_topic(self, value: Optional[DdsCpTopic]) -> "DdsCpServiceInstanceEventBuilder":
        """Set dds_event_topic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_event_topic = value
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


    def build(self) -> DdsCpServiceInstanceEvent:
        """Build and return the DdsCpServiceInstanceEvent instance with validation."""
        self._validate_instance()
        pass
        return self._obj