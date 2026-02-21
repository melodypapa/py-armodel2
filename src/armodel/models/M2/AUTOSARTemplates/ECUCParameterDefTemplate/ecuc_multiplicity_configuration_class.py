"""EcucMultiplicityConfigurationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_configuration_class import (
    EcucAbstractConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class EcucMultiplicityConfigurationClass(EcucAbstractConfigurationClass):
    """AUTOSAR EcucMultiplicityConfigurationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize EcucMultiplicityConfigurationClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize EcucMultiplicityConfigurationClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucMultiplicityConfigurationClass, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "EcucMultiplicityConfigurationClass":
        """Deserialize XML element to EcucMultiplicityConfigurationClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucMultiplicityConfigurationClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(EcucMultiplicityConfigurationClass, cls).deserialize(element)



class EcucMultiplicityConfigurationClassBuilder:
    """Builder for EcucMultiplicityConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucMultiplicityConfigurationClass = EcucMultiplicityConfigurationClass()

    def build(self) -> EcucMultiplicityConfigurationClass:
        """Build and return EcucMultiplicityConfigurationClass object.

        Returns:
            EcucMultiplicityConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
