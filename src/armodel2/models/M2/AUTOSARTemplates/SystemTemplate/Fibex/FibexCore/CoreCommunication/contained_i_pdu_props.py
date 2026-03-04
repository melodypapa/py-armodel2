"""ContainedIPduProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ContainedIPduProps(ARObject):
    """AUTOSAR ContainedIPduProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONTAINED-I-PDU-PROPS"


    collection: Optional[Any]
    contained_pdu_ref: Optional[ARRef]
    header_id_long: Optional[PositiveInteger]
    header_id_short: Optional[PositiveInteger]
    offset: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    timeout: Optional[TimeValue]
    trigger_ref: Optional[PduCollectionTriggerEnum]
    update: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "COLLECTION": lambda obj, elem: setattr(obj, "collection", SerializationHelper.deserialize_by_tag(elem, "any (ContainedIPdu)")),
        "CONTAINED-PDU-REF": lambda obj, elem: setattr(obj, "contained_pdu_ref", ARRef.deserialize(elem)),
        "HEADER-ID-LONG": lambda obj, elem: setattr(obj, "header_id_long", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "HEADER-ID-SHORT": lambda obj, elem: setattr(obj, "header_id_short", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "OFFSET": lambda obj, elem: setattr(obj, "offset", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIMEOUT": lambda obj, elem: setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRIGGER-REF": lambda obj, elem: setattr(obj, "trigger_ref", PduCollectionTriggerEnum.deserialize(elem)),
        "UPDATE": lambda obj, elem: setattr(obj, "update", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()
        self.collection: Optional[Any] = None
        self.contained_pdu_ref: Optional[ARRef] = None
        self.header_id_long: Optional[PositiveInteger] = None
        self.header_id_short: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.timeout: Optional[TimeValue] = None
        self.trigger_ref: Optional[PduCollectionTriggerEnum] = None
        self.update: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ContainedIPduProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ContainedIPduProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collection
        if self.collection is not None:
            serialized = SerializationHelper.serialize_item(self.collection, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contained_pdu_ref
        if self.contained_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.contained_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINED-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_id_long
        if self.header_id_long is not None:
            serialized = SerializationHelper.serialize_item(self.header_id_long, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize header_id_short
        if self.header_id_short is not None:
            serialized = SerializationHelper.serialize_item(self.header_id_short, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEADER-ID-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = SerializationHelper.serialize_item(self.offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update
        if self.update is not None:
            serialized = SerializationHelper.serialize_item(self.update, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainedIPduProps":
        """Deserialize XML element to ContainedIPduProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ContainedIPduProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ContainedIPduProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COLLECTION":
                setattr(obj, "collection", SerializationHelper.deserialize_by_tag(child, "any (ContainedIPdu)"))
            elif tag == "CONTAINED-PDU-REF":
                setattr(obj, "contained_pdu_ref", ARRef.deserialize(child))
            elif tag == "HEADER-ID-LONG":
                setattr(obj, "header_id_long", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "HEADER-ID-SHORT":
                setattr(obj, "header_id_short", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "OFFSET":
                setattr(obj, "offset", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIMEOUT":
                setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRIGGER-REF":
                setattr(obj, "trigger_ref", PduCollectionTriggerEnum.deserialize(child))
            elif tag == "UPDATE":
                setattr(obj, "update", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ContainedIPduPropsBuilder(BuilderBase):
    """Builder for ContainedIPduProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ContainedIPduProps = ContainedIPduProps()


    def with_collection(self, value: Optional[any (ContainedIPdu)]) -> "ContainedIPduPropsBuilder":
        """Set collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection = value
        return self

    def with_contained_pdu(self, value: Optional[PduTriggering]) -> "ContainedIPduPropsBuilder":
        """Set contained_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.contained_pdu = value
        return self

    def with_header_id_long(self, value: Optional[PositiveInteger]) -> "ContainedIPduPropsBuilder":
        """Set header_id_long attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_id_long = value
        return self

    def with_header_id_short(self, value: Optional[PositiveInteger]) -> "ContainedIPduPropsBuilder":
        """Set header_id_short attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.header_id_short = value
        return self

    def with_offset(self, value: Optional[PositiveInteger]) -> "ContainedIPduPropsBuilder":
        """Set offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "ContainedIPduPropsBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_timeout(self, value: Optional[TimeValue]) -> "ContainedIPduPropsBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout = value
        return self

    def with_trigger(self, value: Optional[PduCollectionTriggerEnum]) -> "ContainedIPduPropsBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trigger = value
        return self

    def with_update(self, value: Optional[PositiveInteger]) -> "ContainedIPduPropsBuilder":
        """Set update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.update = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "collection",
        "containedPdu",
        "headerIdLong",
        "headerIdShort",
        "offset",
        "priority",
        "timeout",
        "trigger",
        "update",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ContainedIPduProps:
        """Build and return the ContainedIPduProps instance with validation."""
        self._validate_instance()
        return self._obj