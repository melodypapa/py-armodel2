"""ArParameterInImplementationDataInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ArParameterInImplementationDataInstanceRef(ARObject):
    """AUTOSAR ArParameterInImplementationDataInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_datas: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_parameter: Optional[ParameterDataPrototype]
    target_data: Optional[Any]
    def __init__(self) -> None:
        """Initialize ArParameterInImplementationDataInstanceRef."""
        super().__init__()
        self.context_datas: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_parameter: Optional[ParameterDataPrototype] = None
        self.target_data: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArParameterInImplementationDataInstanceRef":
        """Deserialize XML element to ArParameterInImplementationDataInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArParameterInImplementationDataInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_datas (list from container "CONTEXT-DATAS")
        obj.context_datas = []
        container = ARObject._find_child_element(element, "CONTEXT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_datas.append(child_value)

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE")
        if child is not None:
            port_prototype_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse root_parameter
        child = ARObject._find_child_element(element, "ROOT-PARAMETER")
        if child is not None:
            root_parameter_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.root_parameter = root_parameter_value

        # Parse target_data
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_value = child.text
            obj.target_data = target_data_value

        return obj



class ArParameterInImplementationDataInstanceRefBuilder:
    """Builder for ArParameterInImplementationDataInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArParameterInImplementationDataInstanceRef = ArParameterInImplementationDataInstanceRef()

    def build(self) -> ArParameterInImplementationDataInstanceRef:
        """Build and return ArParameterInImplementationDataInstanceRef object.

        Returns:
            ArParameterInImplementationDataInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
