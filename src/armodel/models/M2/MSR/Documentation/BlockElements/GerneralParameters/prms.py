"""Prms AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_GerneralParameters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class Prms(Paginateable):
    """AUTOSAR Prms."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label: Optional[MultilanguageLongName]
    prm: Any
    def __init__(self) -> None:
        """Initialize Prms."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.prm: Any = None

    def serialize(self) -> ET.Element:
        """Serialize Prms to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Prms, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label
        if self.label is not None:
            serialized = ARObject._serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prm
        if self.prm is not None:
            serialized = ARObject._serialize_item(self.prm, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Prms":
        """Deserialize XML element to Prms object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Prms object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Prms, cls).deserialize(element)

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_with_type(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse prm
        child = ARObject._find_child_element(element, "PRM")
        if child is not None:
            prm_value = child.text
            obj.prm = prm_value

        return obj



class PrmsBuilder:
    """Builder for Prms."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Prms = Prms()

    def build(self) -> Prms:
        """Build and return Prms object.

        Returns:
            Prms instance
        """
        # TODO: Add validation
        return self._obj
