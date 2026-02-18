"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from abc import ABC, abstractmethod


class DataPrototypeInPortInterfaceInstanceRef(ARObject, ABC):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    abstract_base: Optional[PortInterface]
    context_datas: list[Any]
    root_data: Optional[AutosarDataPrototype]
    target_data: DataPrototype
    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceInstanceRef."""
        super().__init__()
        self.abstract_base: Optional[PortInterface] = None
        self.context_datas: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target_data: DataPrototype = None


class DataPrototypeInPortInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceInstanceRef = DataPrototypeInPortInterfaceInstanceRef()

    def build(self) -> DataPrototypeInPortInterfaceInstanceRef:
        """Build and return DataPrototypeInPortInterfaceInstanceRef object.

        Returns:
            DataPrototypeInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
