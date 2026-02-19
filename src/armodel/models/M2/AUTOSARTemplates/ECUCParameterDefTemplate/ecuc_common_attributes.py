"""EcucCommonAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 48)

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
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_value_configuration_class import (
    EcucValueConfigurationClass,
)
from abc import ABC, abstractmethod


class EcucCommonAttributes(EcucDefinitionElement, ABC):
    """AUTOSAR EcucCommonAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    multiplicities: list[EcucMultiplicityConfigurationClass]
    origin: Optional[String]
    post_build_variant: Optional[Boolean]
    requires_index: Optional[Boolean]
    value_configs: list[EcucValueConfigurationClass]
    def __init__(self) -> None:
        """Initialize EcucCommonAttributes."""
        super().__init__()
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None
        self.value_configs: list[EcucValueConfigurationClass] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucCommonAttributes":
        """Deserialize XML element to EcucCommonAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucCommonAttributes object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        # Parse value_configs (list)
        obj.value_configs = []
        for child in ARObject._find_all_child_elements(element, "VALUE-CONFIGS"):
            value_configs_value = ARObject._deserialize_by_tag(child, "EcucValueConfigurationClass")
            obj.value_configs.append(value_configs_value)

        return obj



class EcucCommonAttributesBuilder:
    """Builder for EcucCommonAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucCommonAttributes = EcucCommonAttributes()

    def build(self) -> EcucCommonAttributes:
        """Build and return EcucCommonAttributes object.

        Returns:
            EcucCommonAttributes instance
        """
        # TODO: Add validation
        return self._obj
