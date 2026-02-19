"""FlexrayTpPduPool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 596)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayTpPduPool(Identifiable):
    """AUTOSAR FlexrayTpPduPool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    n_pdus: list[NPdu]
    def __init__(self) -> None:
        """Initialize FlexrayTpPduPool."""
        super().__init__()
        self.n_pdus: list[NPdu] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpPduPool to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpPduPool, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize n_pdus (list to container "N-PDUS")
        if self.n_pdus:
            wrapper = ET.Element("N-PDUS")
            for item in self.n_pdus:
                serialized = ARObject._serialize_item(item, "NPdu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpPduPool":
        """Deserialize XML element to FlexrayTpPduPool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpPduPool object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpPduPool, cls).deserialize(element)

        # Parse n_pdus (list from container "N-PDUS")
        obj.n_pdus = []
        container = ARObject._find_child_element(element, "N-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.n_pdus.append(child_value)

        return obj



class FlexrayTpPduPoolBuilder:
    """Builder for FlexrayTpPduPool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpPduPool = FlexrayTpPduPool()

    def build(self) -> FlexrayTpPduPool:
        """Build and return FlexrayTpPduPool object.

        Returns:
            FlexrayTpPduPool instance
        """
        # TODO: Add validation
        return self._obj
