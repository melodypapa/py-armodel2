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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortPrototypeBlueprint, cls).deserialize(element)

        # Parse init_value_refs (list from container "INIT-VALUES")
        obj.init_value_refs = []
        container = ARObject._find_child_element(element, "INIT-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.init_value_refs.append(child_value)

        # Parse interface
        child = ARObject._find_child_element(element, "INTERFACE")
        if child is not None:
            interface_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.interface = interface_value

        # Parse provided_coms (list from container "PROVIDED-COMS")
        obj.provided_coms = []
        container = ARObject._find_child_element(element, "PROVIDED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_coms.append(child_value)

        # Parse required_coms (list from container "REQUIRED-COMS")
        obj.required_coms = []
        container = ARObject._find_child_element(element, "REQUIRED-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_coms.append(child_value)

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
