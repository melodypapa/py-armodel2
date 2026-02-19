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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvDataInterface":
        """Deserialize XML element to NvDataInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvDataInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvDataInterface, cls).deserialize(element)

        # Parse nv_data_refs (list from container "NV-DATAS")
        obj.nv_data_refs = []
        container = ARObject._find_child_element(element, "NV-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_data_refs.append(child_value)

        return obj



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
