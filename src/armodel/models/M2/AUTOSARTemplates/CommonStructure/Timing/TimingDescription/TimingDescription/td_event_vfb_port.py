"""TDEventVfbPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)
from abc import ABC, abstractmethod


class TDEventVfbPort(TDEventVfb, ABC):
    """AUTOSAR TDEventVfbPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_external: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventVfbPort."""
        super().__init__()
        self.is_external: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_prototype_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbPort":
        """Deserialize XML element to TDEventVfbPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVfbPort object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse is_external
        child = ARObject._find_child_element(element, "IS-EXTERNAL")
        if child is not None:
            is_external_value = child.text
            obj.is_external = is_external_value

        # Parse port_ref
        child = ARObject._find_child_element(element, "PORT")
        if child is not None:
            port_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.port_ref = port_ref_value

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE")
        if child is not None:
            port_prototype_ref_value = ARObject._deserialize_by_tag(child, "PortPrototypeBlueprint")
            obj.port_prototype_ref = port_prototype_ref_value

        return obj



class TDEventVfbPortBuilder:
    """Builder for TDEventVfbPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbPort = TDEventVfbPort()

    def build(self) -> TDEventVfbPort:
        """Build and return TDEventVfbPort object.

        Returns:
            TDEventVfbPort instance
        """
        # TODO: Add validation
        return self._obj
