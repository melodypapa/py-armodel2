"""Annotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 334)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_MSR_Documentation_Annotation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class Annotation(GeneralAnnotation):
    """AUTOSAR Annotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize Annotation."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize Annotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Annotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Annotation":
        """Deserialize XML element to Annotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Annotation object
        """
        # Delegate to parent class to handle inherited attributes
        return super(Annotation, cls).deserialize(element)



class AnnotationBuilder:
    """Builder for Annotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Annotation = Annotation()

    def build(self) -> Annotation:
        """Build and return Annotation object.

        Returns:
            Annotation instance
        """
        # TODO: Add validation
        return self._obj
