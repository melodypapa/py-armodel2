"""Keyword AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 454)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Keyword.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class Keyword(Identifiable):
    """AUTOSAR Keyword."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    abbr_name: NameToken
    classifications: list[NameToken]
    def __init__(self) -> None:
        """Initialize Keyword."""
        super().__init__()
        self.abbr_name: NameToken = None
        self.classifications: list[NameToken] = []

    def serialize(self) -> ET.Element:
        """Serialize Keyword to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Keyword, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize abbr_name
        if self.abbr_name is not None:
            serialized = ARObject._serialize_item(self.abbr_name, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ABBR-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize classifications (list to container "CLASSIFICATIONS")
        if self.classifications:
            wrapper = ET.Element("CLASSIFICATIONS")
            for item in self.classifications:
                serialized = ARObject._serialize_item(item, "NameToken")
                if serialized is not None:
                    child_elem = ET.Element("CLASSIFICATION")
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
    def deserialize(cls, element: ET.Element) -> "Keyword":
        """Deserialize XML element to Keyword object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Keyword object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Keyword, cls).deserialize(element)

        # Parse abbr_name
        child = ARObject._find_child_element(element, "ABBR-NAME")
        if child is not None:
            abbr_name_value = child.text
            obj.abbr_name = abbr_name_value

        # Parse classifications (list from container "CLASSIFICATIONS")
        obj.classifications = []
        container = ARObject._find_child_element(element, "CLASSIFICATIONS")
        if container is not None:
            for child in container:
                # Extract primitive value (NameToken) as text
                child_value = child.text
                if child_value is not None:
                    obj.classifications.append(child_value)

        return obj



class KeywordBuilder:
    """Builder for Keyword."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Keyword = Keyword()

    def build(self) -> Keyword:
        """Build and return Keyword object.

        Returns:
            Keyword instance
        """
        # TODO: Add validation
        return self._obj
