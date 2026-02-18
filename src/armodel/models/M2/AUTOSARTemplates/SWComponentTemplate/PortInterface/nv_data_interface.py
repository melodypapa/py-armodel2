"""NvDataInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 664)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2041)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataInterface(DataInterface):
    """AUTOSAR NvDataInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nv_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize NvDataInterface."""
        super().__init__()
        self.nv_data_refs: list[ARRef] = []


class NvDataInterfaceBuilder:
    """Builder for NvDataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvDataInterface = NvDataInterface()

    def build(self) -> NvDataInterface:
        """Build and return NvDataInterface object.

        Returns:
            NvDataInterface instance
        """
        # TODO: Add validation
        return self._obj
