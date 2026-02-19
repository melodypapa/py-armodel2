"""ScaleConstr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Limit,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class ScaleConstr(ARObject):
    """AUTOSAR ScaleConstr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    desc: Optional[MultiLanguageOverviewParagraph]
    lower_limit: Optional[Limit]
    short_label: Optional[Identifier]
    upper_limit: Optional[Limit]
    validity: Optional[Any]
    def __init__(self) -> None:
        """Initialize ScaleConstr."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.short_label: Optional[Identifier] = None
        self.upper_limit: Optional[Limit] = None
        self.validity: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ScaleConstr to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize desc
        if self.desc is not None:
            serialized = ARObject._serialize_item(self.desc, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = ARObject._serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = ARObject._serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize validity
        if self.validity is not None:
            serialized = ARObject._serialize_item(self.validity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScaleConstr":
        """Deserialize XML element to ScaleConstr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ScaleConstr object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse lower_limit
        child = ARObject._find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.lower_limit = lower_limit_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse upper_limit
        child = ARObject._find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.upper_limit = upper_limit_value

        # Parse validity
        child = ARObject._find_child_element(element, "VALIDITY")
        if child is not None:
            validity_value = child.text
            obj.validity = validity_value

        return obj



class ScaleConstrBuilder:
    """Builder for ScaleConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ScaleConstr = ScaleConstr()

    def build(self) -> ScaleConstr:
        """Build and return ScaleConstr object.

        Returns:
            ScaleConstr instance
        """
        # TODO: Add validation
        return self._obj
