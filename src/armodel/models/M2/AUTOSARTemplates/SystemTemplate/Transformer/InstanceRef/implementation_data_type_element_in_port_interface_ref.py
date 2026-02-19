"""ImplementationDataTypeElementInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 789)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR ImplementationDataTypeElementInPortInterfaceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contexts: list[Any]
    root_data_ref: Optional[ARRef]
    target: Optional[AbstractImplementationDataType]
    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElementInPortInterfaceRef."""
        super().__init__()
        self.contexts: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target: Optional[AbstractImplementationDataType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """Deserialize XML element to ImplementationDataTypeElementInPortInterfaceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeElementInPortInterfaceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeElementInPortInterfaceRef, cls).deserialize(element)

        # Parse contexts (list from container "CONTEXTS")
        obj.contexts = []
        container = ARObject._find_child_element(element, "CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contexts.append(child_value)

        # Parse root_data_ref
        child = ARObject._find_child_element(element, "ROOT-DATA")
        if child is not None:
            root_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.root_data_ref = root_data_ref_value

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = ARObject._deserialize_by_tag(child, "AbstractImplementationDataType")
            obj.target = target_value

        return obj



class ImplementationDataTypeElementInPortInterfaceRefBuilder:
    """Builder for ImplementationDataTypeElementInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeElementInPortInterfaceRef = ImplementationDataTypeElementInPortInterfaceRef()

    def build(self) -> ImplementationDataTypeElementInPortInterfaceRef:
        """Build and return ImplementationDataTypeElementInPortInterfaceRef object.

        Returns:
            ImplementationDataTypeElementInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
