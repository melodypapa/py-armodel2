"""TransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class TransformationProps(Identifiable, ABC):
    """AUTOSAR TransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize TransformationProps."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize TransformationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationProps":
        """Deserialize XML element to TransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationProps object
        """
        # Delegate to parent class to handle inherited attributes
        return super(TransformationProps, cls).deserialize(element)



class TransformationPropsBuilder:
    """Builder for TransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationProps = TransformationProps()

    def build(self) -> TransformationProps:
        """Build and return TransformationProps object.

        Returns:
            TransformationProps instance
        """
        # TODO: Add validation
        return self._obj
