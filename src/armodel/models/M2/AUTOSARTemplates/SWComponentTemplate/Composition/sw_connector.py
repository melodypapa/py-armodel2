"""SwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2061)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from abc import ABC, abstractmethod


class SwConnector(Identifiable, ABC):
    """AUTOSAR SwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    mapping_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwConnector."""
        super().__init__()
        self.mapping_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mapping_ref
        if self.mapping_ref is not None:
            serialized = ARObject._serialize_item(self.mapping_ref, "PortInterfaceMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwConnector":
        """Deserialize XML element to SwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwConnector, cls).deserialize(element)

        # Parse mapping_ref
        child = ARObject._find_child_element(element, "MAPPING-REF")
        if child is not None:
            mapping_ref_value = ARRef.deserialize(child)
            obj.mapping_ref = mapping_ref_value

        return obj



class SwConnectorBuilder:
    """Builder for SwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwConnector = SwConnector()

    def build(self) -> SwConnector:
        """Build and return SwConnector object.

        Returns:
            SwConnector instance
        """
        # TODO: Add validation
        return self._obj
