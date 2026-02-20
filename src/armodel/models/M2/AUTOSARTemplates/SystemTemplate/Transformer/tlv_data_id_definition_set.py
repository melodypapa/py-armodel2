"""TlvDataIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tlv_data_ids: list[TlvDataIdDefinition]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinitionSet."""
        super().__init__()
        self.tlv_data_ids: list[TlvDataIdDefinition] = []

    def serialize(self) -> ET.Element:
        """Serialize TlvDataIdDefinitionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlvDataIdDefinitionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tlv_data_ids (list to container "TLV-DATA-IDS")
        if self.tlv_data_ids:
            wrapper = ET.Element("TLV-DATA-IDS")
            for item in self.tlv_data_ids:
                serialized = ARObject._serialize_item(item, "TlvDataIdDefinition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinitionSet":
        """Deserialize XML element to TlvDataIdDefinitionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinitionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlvDataIdDefinitionSet, cls).deserialize(element)

        # Parse tlv_data_ids (list from container "TLV-DATA-IDS")
        obj.tlv_data_ids = []
        container = ARObject._find_child_element(element, "TLV-DATA-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tlv_data_ids.append(child_value)

        return obj



class TlvDataIdDefinitionSetBuilder:
    """Builder for TlvDataIdDefinitionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinitionSet = TlvDataIdDefinitionSet()

    def build(self) -> TlvDataIdDefinitionSet:
        """Build and return TlvDataIdDefinitionSet object.

        Returns:
            TlvDataIdDefinitionSet instance
        """
        # TODO: Add validation
        return self._obj
