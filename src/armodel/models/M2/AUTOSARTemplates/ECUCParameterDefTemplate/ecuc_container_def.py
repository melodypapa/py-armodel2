"""EcucContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 36)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)
from abc import ABC, abstractmethod


class EcucContainerDef(EcucDefinitionElement, ABC):
    """AUTOSAR EcucContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    destination_uris: list[EcucDestinationUriDef]
    multiplicities: list[EcucMultiplicityConfigurationClass]
    origin: Optional[String]
    post_build_variant: Optional[Boolean]
    requires_index: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucContainerDef."""
        super().__init__()
        self.destination_uris: list[EcucDestinationUriDef] = []
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerDef":
        """Deserialize XML element to EcucContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucContainerDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_uris (list)
        obj.destination_uris = []
        for child in ARObject._find_all_child_elements(element, "DESTINATION-URIS"):
            destination_uris_value = ARObject._deserialize_by_tag(child, "EcucDestinationUriDef")
            obj.destination_uris.append(destination_uris_value)

        # Parse multiplicities (list)
        obj.multiplicities = []
        for child in ARObject._find_all_child_elements(element, "MULTIPLICITIES"):
            multiplicities_value = ARObject._deserialize_by_tag(child, "EcucMultiplicityConfigurationClass")
            obj.multiplicities.append(multiplicities_value)

        # Parse origin
        child = ARObject._find_child_element(element, "ORIGIN")
        if child is not None:
            origin_value = child.text
            obj.origin = origin_value

        # Parse post_build_variant
        child = ARObject._find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        # Parse requires_index
        child = ARObject._find_child_element(element, "REQUIRES-INDEX")
        if child is not None:
            requires_index_value = child.text
            obj.requires_index = requires_index_value

        return obj



class EcucContainerDefBuilder:
    """Builder for EcucContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerDef = EcucContainerDef()

    def build(self) -> EcucContainerDef:
        """Build and return EcucContainerDef object.

        Returns:
            EcucContainerDef instance
        """
        # TODO: Add validation
        return self._obj
