"""DataPrototypeInSenderReceiverInterfaceInstanceRef AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_interface: Optional[Any]
    context_datas: list[Any]
    root_data_prototype_in_sr: Optional[AutosarDataPrototype]
    target_data_prototype_in_sr: Optional[DataPrototype]
    def __init__(self) -> None:
        """Initialize DataPrototypeInSenderReceiverInterfaceInstanceRef."""
        super().__init__()
        self.base_interface: Optional[Any] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_sr: Optional[AutosarDataPrototype] = None
        self.target_data_prototype_in_sr: Optional[DataPrototype] = None


class DataPrototypeInSenderReceiverInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSenderReceiverInterfaceInstanceRef = DataPrototypeInSenderReceiverInterfaceInstanceRef()

    def build(self) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """Build and return DataPrototypeInSenderReceiverInterfaceInstanceRef object.

        Returns:
            DataPrototypeInSenderReceiverInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
