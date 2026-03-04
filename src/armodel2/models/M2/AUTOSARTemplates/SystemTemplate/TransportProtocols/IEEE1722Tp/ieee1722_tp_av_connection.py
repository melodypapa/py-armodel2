"""IEEE1722TpAvConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 639)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import IEEE1722TpConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAvConnection(IEEE1722TpConnection, ABC):
    """AUTOSAR IEEE1722TpAvConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max_transit_time: Optional[TimeValue]
    sdu_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MAX-TRANSIT-TIME": lambda obj, elem: setattr(obj, "max_transit_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SDU-REFS": lambda obj, elem: [obj.sdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAvConnection."""
        super().__init__()
        self.max_transit_time: Optional[TimeValue] = None
        self.sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAvConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAvConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_transit_time
        if self.max_transit_time is not None:
            serialized = SerializationHelper.serialize_item(self.max_transit_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-TRANSIT-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_refs (list to container "SDU-REFS")
        if self.sdu_refs:
            wrapper = ET.Element("SDU-REFS")
            for item in self.sdu_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("SDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAvConnection":
        """Deserialize XML element to IEEE1722TpAvConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAvConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAvConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-TRANSIT-TIME":
                setattr(obj, "max_transit_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sdu_refs.append(ARRef.deserialize(item_elem))

        return obj



class IEEE1722TpAvConnectionBuilder(IEEE1722TpConnectionBuilder):
    """Builder for IEEE1722TpAvConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAvConnection = IEEE1722TpAvConnection()


    def with_max_transit_time(self, value: Optional[TimeValue]) -> "IEEE1722TpAvConnectionBuilder":
        """Set max_transit_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_transit_time = value
        return self

    def with_sdus(self, items: list[PduTriggering]) -> "IEEE1722TpAvConnectionBuilder":
        """Set sdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdus = list(items) if items else []
        return self


    def add_sdu(self, item: PduTriggering) -> "IEEE1722TpAvConnectionBuilder":
        """Add a single item to sdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdus.append(item)
        return self

    def clear_sdus(self) -> "IEEE1722TpAvConnectionBuilder":
        """Clear all items from sdus list.

        Returns:
            self for method chaining
        """
        self._obj.sdus = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxTransitTime",
        "sdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> IEEE1722TpAvConnection:
        """Build and return the IEEE1722TpAvConnection instance (abstract)."""
        raise NotImplementedError