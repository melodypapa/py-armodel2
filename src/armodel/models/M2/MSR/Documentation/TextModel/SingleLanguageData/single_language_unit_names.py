"""SingleLanguageUnitNames AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_SingleLanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextModel.mixed_content_for_unit_names import (
    MixedContentForUnitNames,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SingleLanguageUnitNames(MixedContentForUnitNames):
    """AUTOSAR SingleLanguageUnitNames."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SingleLanguageUnitNames."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SingleLanguageUnitNames to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SingleLanguageUnitNames, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SingleLanguageUnitNames":
        """Deserialize XML element to SingleLanguageUnitNames object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SingleLanguageUnitNames object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SingleLanguageUnitNames, cls).deserialize(element)



class SingleLanguageUnitNamesBuilder:
    """Builder for SingleLanguageUnitNames."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageUnitNames = SingleLanguageUnitNames()

    def build(self) -> SingleLanguageUnitNames:
        """Build and return SingleLanguageUnitNames object.

        Returns:
            SingleLanguageUnitNames instance
        """
        # TODO: Add validation
        return self._obj
