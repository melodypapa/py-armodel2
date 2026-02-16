"""NvDataInterface AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataInterface(DataInterface):
    """AUTOSAR NvDataInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "nv_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # nvDatas
    }

    def __init__(self) -> None:
        """Initialize NvDataInterface."""
        super().__init__()
        self.nv_datas: list[VariableDataPrototype] = []


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
