"""DataPrototypeInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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


class DataPrototypeInPortInterfaceInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInPortInterfaceInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "abstract_base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortInterface,
        ),  # abstractBase
        "context_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # contextDatas
        "root_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataPrototype,
        ),  # rootData
        "target_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DataPrototype,
        ),  # targetData
    }

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
