"""DataPrototypeInClientServerInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 788)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInClientServerInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize DataPrototypeInClientServerInterfaceInstanceRef."""
        super().__init__()
        self.base: Optional[ClientServerInterface] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_cs: Optional[AutosarDataPrototype] = None
        self.target_data_prototype_in_cs: Optional[DataPrototype] = None


class DataPrototypeInClientServerInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInClientServerInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInClientServerInterfaceInstanceRef = DataPrototypeInClientServerInterfaceInstanceRef()

    def build(self) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """Build and return DataPrototypeInClientServerInterfaceInstanceRef object.

        Returns:
            DataPrototypeInClientServerInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
