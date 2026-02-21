"""FMConditionByFeaturesAndAttributes AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class FMConditionByFeaturesAndAttributes(ARObject):
    """AUTOSAR FMConditionByFeaturesAndAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize FMConditionByFeaturesAndAttributes."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize FMConditionByFeaturesAndAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMConditionByFeaturesAndAttributes, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "FMConditionByFeaturesAndAttributes":
        """Deserialize XML element to FMConditionByFeaturesAndAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMConditionByFeaturesAndAttributes object
        """
        # Delegate to parent class to handle inherited attributes
        return super(FMConditionByFeaturesAndAttributes, cls).deserialize(element)



class FMConditionByFeaturesAndAttributesBuilder:
    """Builder for FMConditionByFeaturesAndAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMConditionByFeaturesAndAttributes = FMConditionByFeaturesAndAttributes()

    def build(self) -> FMConditionByFeaturesAndAttributes:
        """Build and return FMConditionByFeaturesAndAttributes object.

        Returns:
            FMConditionByFeaturesAndAttributes instance
        """
        # TODO: Add validation
        return self._obj
