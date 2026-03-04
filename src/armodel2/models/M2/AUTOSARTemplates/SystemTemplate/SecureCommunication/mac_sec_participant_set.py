"""MacSecParticipantSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacSecParticipantSet(ARElement):
    """AUTOSAR MacSecParticipantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-SEC-PARTICIPANT-SET"


    ethernet_cluster_ref: Optional[ARRef]
    mka_participants: list[MacSecKayParticipant]
    _DESERIALIZE_DISPATCH = {
        "ETHERNET-CLUSTER-REF": lambda obj, elem: setattr(obj, "ethernet_cluster_ref", ARRef.deserialize(elem)),
        "MKA-PARTICIPANTS": lambda obj, elem: obj.mka_participants.append(SerializationHelper.deserialize_by_tag(elem, "MacSecKayParticipant")),
    }


    def __init__(self) -> None:
        """Initialize MacSecParticipantSet."""
        super().__init__()
        self.ethernet_cluster_ref: Optional[ARRef] = None
        self.mka_participants: list[MacSecKayParticipant] = []

    def serialize(self) -> ET.Element:
        """Serialize MacSecParticipantSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecParticipantSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ethernet_cluster_ref
        if self.ethernet_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ethernet_cluster_ref, "EthernetCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHERNET-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mka_participants (list to container "MKA-PARTICIPANTS")
        if self.mka_participants:
            wrapper = ET.Element("MKA-PARTICIPANTS")
            for item in self.mka_participants:
                serialized = SerializationHelper.serialize_item(item, "MacSecKayParticipant")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecParticipantSet":
        """Deserialize XML element to MacSecParticipantSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecParticipantSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecParticipantSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ETHERNET-CLUSTER-REF":
                setattr(obj, "ethernet_cluster_ref", ARRef.deserialize(child))
            elif tag == "MKA-PARTICIPANTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mka_participants.append(SerializationHelper.deserialize_by_tag(item_elem, "MacSecKayParticipant"))

        return obj



class MacSecParticipantSetBuilder(ARElementBuilder):
    """Builder for MacSecParticipantSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecParticipantSet = MacSecParticipantSet()


    def with_ethernet_cluster(self, value: Optional[EthernetCluster]) -> "MacSecParticipantSetBuilder":
        """Set ethernet_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ethernet_cluster = value
        return self

    def with_mka_participants(self, items: list[MacSecKayParticipant]) -> "MacSecParticipantSetBuilder":
        """Set mka_participants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = list(items) if items else []
        return self


    def add_mka_participant(self, item: MacSecKayParticipant) -> "MacSecParticipantSetBuilder":
        """Add a single item to mka_participants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mka_participants.append(item)
        return self

    def clear_mka_participants(self) -> "MacSecParticipantSetBuilder":
        """Clear all items from mka_participants list.

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ethernetCluster",
        "mkaParticipant",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MacSecParticipantSet:
        """Build and return the MacSecParticipantSet instance with validation."""
        self._validate_instance()
        return self._obj