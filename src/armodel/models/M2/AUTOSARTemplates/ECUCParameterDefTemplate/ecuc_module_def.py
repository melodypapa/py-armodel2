"""EcucModuleDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 32)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucModuleDef(EcucDefinitionElement):
    """AUTOSAR EcucModuleDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    api_service_prefix: Optional[CIdentifier]
    containers: list[EcucContainerDef]
    post_build_variant: Optional[Boolean]
    refined_module: Optional[EcucModuleDef]
    supporteds: list[Any]
    def __init__(self) -> None:
        """Initialize EcucModuleDef."""
        super().__init__()
        self.api_service_prefix: Optional[CIdentifier] = None
        self.containers: list[EcucContainerDef] = []
        self.post_build_variant: Optional[Boolean] = None
        self.refined_module: Optional[EcucModuleDef] = None
        self.supporteds: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleDef":
        """Deserialize XML element to EcucModuleDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucModuleDef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse api_service_prefix
        child = ARObject._find_child_element(element, "API-SERVICE-PREFIX")
        if child is not None:
            api_service_prefix_value = child.text
            obj.api_service_prefix = api_service_prefix_value

        # Parse containers (list)
        obj.containers = []
        for child in ARObject._find_all_child_elements(element, "CONTAINERS"):
            containers_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.containers.append(containers_value)

        # Parse post_build_variant
        child = ARObject._find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        # Parse refined_module
        child = ARObject._find_child_element(element, "REFINED-MODULE")
        if child is not None:
            refined_module_value = ARObject._deserialize_by_tag(child, "EcucModuleDef")
            obj.refined_module = refined_module_value

        # Parse supporteds (list)
        obj.supporteds = []
        for child in ARObject._find_all_child_elements(element, "SUPPORTEDS"):
            supporteds_value = child.text
            obj.supporteds.append(supporteds_value)

        return obj



class EcucModuleDefBuilder:
    """Builder for EcucModuleDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleDef = EcucModuleDef()

    def build(self) -> EcucModuleDef:
        """Build and return EcucModuleDef object.

        Returns:
            EcucModuleDef instance
        """
        # TODO: Add validation
        return self._obj
