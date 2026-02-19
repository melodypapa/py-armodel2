"""PortPrototypeBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Port.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class PortPrototypeBlueprint(ARElement):
    """AUTOSAR PortPrototypeBlueprint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value_refs: list[ARRef]
    interface: PortInterface
    provided_coms: list[PPortComSpec]
    required_coms: list[RPortComSpec]
    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprint."""
        super().__init__()
        self.init_value_refs: list[ARRef] = []
        self.interface: PortInterface = None
        self.provided_coms: list[PPortComSpec] = []
        self.required_coms: list[RPortComSpec] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototypeBlueprint":
        """Deserialize XML element to PortPrototypeBlueprint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototypeBlueprint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse init_value_refs (list)
        obj.init_value_refs = []
        for child in ARObject._find_all_child_elements(element, "INIT-VALUES"):
            init_value_refs_value = ARObject._deserialize_by_tag(child, "PortPrototypeBlueprint")
            obj.init_value_refs.append(init_value_refs_value)

        # Parse interface
        child = ARObject._find_child_element(element, "INTERFACE")
        if child is not None:
            interface_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.interface = interface_value

        # Parse provided_coms (list)
        obj.provided_coms = []
        for child in ARObject._find_all_child_elements(element, "PROVIDED-COMS"):
            provided_coms_value = ARObject._deserialize_by_tag(child, "PPortComSpec")
            obj.provided_coms.append(provided_coms_value)

        # Parse required_coms (list)
        obj.required_coms = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-COMS"):
            required_coms_value = ARObject._deserialize_by_tag(child, "RPortComSpec")
            obj.required_coms.append(required_coms_value)

        return obj



class PortPrototypeBlueprintBuilder:
    """Builder for PortPrototypeBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprint = PortPrototypeBlueprint()

    def build(self) -> PortPrototypeBlueprint:
        """Build and return PortPrototypeBlueprint object.

        Returns:
            PortPrototypeBlueprint instance
        """
        # TODO: Add validation
        return self._obj
