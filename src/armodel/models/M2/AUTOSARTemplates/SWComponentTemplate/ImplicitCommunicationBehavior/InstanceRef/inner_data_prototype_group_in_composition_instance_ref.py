"""InnerDataPrototypeGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 954)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)


class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerDataPrototypeGroupInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    context_sws: list[Any]
    target_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InnerDataPrototypeGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_data_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """Deserialize XML element to InnerDataPrototypeGroupInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InnerDataPrototypeGroupInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse context_sws (list)
        obj.context_sws = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-SWS"):
            context_sws_value = child.text
            obj.context_sws.append(context_sws_value)

        # Parse target_data_ref
        child = ARObject._find_child_element(element, "TARGET-DATA")
        if child is not None:
            target_data_ref_value = ARObject._deserialize_by_tag(child, "DataPrototypeGroup")
            obj.target_data_ref = target_data_ref_value

        return obj



class InnerDataPrototypeGroupInCompositionInstanceRefBuilder:
    """Builder for InnerDataPrototypeGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerDataPrototypeGroupInCompositionInstanceRef = InnerDataPrototypeGroupInCompositionInstanceRef()

    def build(self) -> InnerDataPrototypeGroupInCompositionInstanceRef:
        """Build and return InnerDataPrototypeGroupInCompositionInstanceRef object.

        Returns:
            InnerDataPrototypeGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
