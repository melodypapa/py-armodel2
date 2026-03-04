"""OrderedMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class OrderedMaster(ARObject):
    """AUTOSAR OrderedMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ORDERED-MASTER"


    index: Optional[PositiveInteger]
    time_sync_server_configuration_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INDEX": lambda obj, elem: setattr(obj, "index", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-SYNC-SERVER-CONFIGURATION-REF": lambda obj, elem: setattr(obj, "time_sync_server_configuration_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize OrderedMaster."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
        self.time_sync_server_configuration_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize OrderedMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(OrderedMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize index
        if self.index is not None:
            serialized = SerializationHelper.serialize_item(self.index, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_configuration_ref
        if self.time_sync_server_configuration_ref is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_server_configuration_ref, "TimeSyncServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-CONFIGURATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OrderedMaster":
        """Deserialize XML element to OrderedMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OrderedMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OrderedMaster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INDEX":
                setattr(obj, "index", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-SYNC-SERVER-CONFIGURATION-REF":
                setattr(obj, "time_sync_server_configuration_ref", ARRef.deserialize(child))

        return obj



class OrderedMasterBuilder(BuilderBase):
    """Builder for OrderedMaster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: OrderedMaster = OrderedMaster()


    def with_index(self, value: Optional[PositiveInteger]) -> "OrderedMasterBuilder":
        """Set index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.index = value
        return self

    def with_time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> "OrderedMasterBuilder":
        """Set time_sync_server_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync_server_configuration = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "index",
        "timeSyncServerConfiguration",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> OrderedMaster:
        """Build and return the OrderedMaster instance with validation."""
        self._validate_instance()
        return self._obj