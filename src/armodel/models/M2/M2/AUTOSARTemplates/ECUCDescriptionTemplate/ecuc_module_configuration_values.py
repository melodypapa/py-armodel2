"""EcucModuleConfigurationValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 441)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class EcucModuleConfigurationValues(ARElement):
    """AUTOSAR EcucModuleConfigurationValues."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "containers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucContainerValue,
        ),  # containers
        "definition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucModuleDef,
        ),  # definition
        "ecuc_def_edition": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ecucDefEdition
        "implementation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # implementation
        "module": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswImplementation,
        ),  # module
        "post_build_variant": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # postBuildVariant
    }

    def __init__(self) -> None:
        """Initialize EcucModuleConfigurationValues."""
        super().__init__()
        self.containers: list[EcucContainerValue] = []
        self.definition: Optional[EcucModuleDef] = None
        self.ecuc_def_edition: Optional[RevisionLabelString] = None
        self.implementation: Optional[Any] = None
        self.module: Optional[BswImplementation] = None
        self.post_build_variant: Optional[Boolean] = None


class EcucModuleConfigurationValuesBuilder:
    """Builder for EcucModuleConfigurationValues."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucModuleConfigurationValues = EcucModuleConfigurationValues()

    def build(self) -> EcucModuleConfigurationValues:
        """Build and return EcucModuleConfigurationValues object.

        Returns:
            EcucModuleConfigurationValues instance
        """
        # TODO: Add validation
        return self._obj
