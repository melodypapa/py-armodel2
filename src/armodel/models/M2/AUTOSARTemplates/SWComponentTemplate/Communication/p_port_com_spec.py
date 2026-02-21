"""PPortComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 166)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class PPortComSpec(ARObject, ABC):
    """AUTOSAR PPortComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize PPortComSpec."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize PPortComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PPortComSpec, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "PPortComSpec":
        """Deserialize XML element to PPortComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PPortComSpec object
        """
        # Delegate to parent class to handle inherited attributes
        return super(PPortComSpec, cls).deserialize(element)



class PPortComSpecBuilder:
    """Builder for PPortComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortComSpec = PPortComSpec()

    def build(self) -> PPortComSpec:
        """Build and return PPortComSpec object.

        Returns:
            PPortComSpec instance
        """
        # TODO: Add validation
        return self._obj
