"""IEEE1722TpAcfBusPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionTriggerEnum,
)
from abc import ABC, abstractmethod


class IEEE1722TpAcfBusPart(Identifiable, ABC):
    """AUTOSAR IEEE1722TpAcfBusPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    collection_trigger_ref: Optional[PduCollectionTriggerEnum]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBusPart."""
        super().__init__()
        self.collection_trigger_ref: Optional[PduCollectionTriggerEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfBusPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfBusPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize collection_trigger_ref
        if self.collection_trigger_ref is not None:
            serialized = ARObject._serialize_item(self.collection_trigger_ref, "PduCollectionTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBusPart":
        """Deserialize XML element to IEEE1722TpAcfBusPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfBusPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfBusPart, cls).deserialize(element)

        # Parse collection_trigger_ref
        child = ARObject._find_child_element(element, "COLLECTION-TRIGGER")
        if child is not None:
            collection_trigger_ref_value = ARRef.deserialize(child)
            obj.collection_trigger_ref = collection_trigger_ref_value

        return obj



class IEEE1722TpAcfBusPartBuilder:
    """Builder for IEEE1722TpAcfBusPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBusPart = IEEE1722TpAcfBusPart()

    def build(self) -> IEEE1722TpAcfBusPart:
        """Build and return IEEE1722TpAcfBusPart object.

        Returns:
            IEEE1722TpAcfBusPart instance
        """
        # TODO: Add validation
        return self._obj
