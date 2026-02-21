"""MacSecParticipantSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)


class MacSecParticipantSet(ARElement):
    """AUTOSAR MacSecParticipantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ethernet_cluster_ref: Optional[ARRef]
    mka_participants: list[MacSecKayParticipant]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse ethernet_cluster_ref
        child = SerializationHelper.find_child_element(element, "ETHERNET-CLUSTER-REF")
        if child is not None:
            ethernet_cluster_ref_value = ARRef.deserialize(child)
            obj.ethernet_cluster_ref = ethernet_cluster_ref_value

        # Parse mka_participants (list from container "MKA-PARTICIPANTS")
        obj.mka_participants = []
        container = SerializationHelper.find_child_element(element, "MKA-PARTICIPANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mka_participants.append(child_value)

        return obj



class MacSecParticipantSetBuilder:
    """Builder for MacSecParticipantSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecParticipantSet = MacSecParticipantSet()

    def build(self) -> MacSecParticipantSet:
        """Build and return MacSecParticipantSet object.

        Returns:
            MacSecParticipantSet instance
        """
        # TODO: Add validation
        return self._obj
