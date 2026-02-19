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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    root_data_prototype_in_sr_ref: Optional[ARRef]
    target_data_prototype_in_sr_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInSenderReceiverInterfaceInstanceRef."""
        super().__init__()
        self.base_interface: Optional[Any] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_sr_ref: Optional[ARRef] = None
        self.target_data_prototype_in_sr_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInSenderReceiverInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInSenderReceiverInterfaceInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_interface
        child = ARObject._find_child_element(element, "BASE-INTERFACE")
        if child is not None:
            base_interface_value = child.text
            obj.base_interface = base_interface_value

        # Parse context_datas (list)
        obj.context_datas = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-DATAS"):
            context_datas_value = child.text
            obj.context_datas.append(context_datas_value)

        # Parse root_data_prototype_in_sr_ref
        child = ARObject._find_child_element(element, "ROOT-DATA-PROTOTYPE-IN-SR")
        if child is not None:
            root_data_prototype_in_sr_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.root_data_prototype_in_sr_ref = root_data_prototype_in_sr_ref_value

        # Parse target_data_prototype_in_sr_ref
        child = ARObject._find_child_element(element, "TARGET-DATA-PROTOTYPE-IN-SR")
        if child is not None:
            target_data_prototype_in_sr_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.target_data_prototype_in_sr_ref = target_data_prototype_in_sr_ref_value

        return obj



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
