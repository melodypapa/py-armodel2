"""VariableAndParameterInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 124)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR VariableAndParameterInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize VariableAndParameterInterfaceMapping."""
        super().__init__()
        self.data_mapping_refs: list[ARRef] = []


class VariableAndParameterInterfaceMappingBuilder:
    """Builder for VariableAndParameterInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAndParameterInterfaceMapping = VariableAndParameterInterfaceMapping()

    def build(self) -> VariableAndParameterInterfaceMapping:
        """Build and return VariableAndParameterInterfaceMapping object.

        Returns:
            VariableAndParameterInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
