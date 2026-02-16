"""VariableInAtomicSWCTypeInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSWCTypeInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AtomicSwComponentType,
        ),  # base
        "context_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ApplicationComposite),
        ),  # contextDatas
        "port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # portPrototype
        "root_variable_data_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # rootVariableDataPrototype
        "target_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototype,
        ),  # targetData
    }

    def __init__(self) -> None:
        """Initialize VariableInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_variable_data_prototype: Optional[VariableDataPrototype] = None
        self.target_data: Optional[DataPrototype] = None


class VariableInAtomicSWCTypeInstanceRefBuilder:
    """Builder for VariableInAtomicSWCTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableInAtomicSWCTypeInstanceRef = VariableInAtomicSWCTypeInstanceRef()

    def build(self) -> VariableInAtomicSWCTypeInstanceRef:
        """Build and return VariableInAtomicSWCTypeInstanceRef object.

        Returns:
            VariableInAtomicSWCTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
