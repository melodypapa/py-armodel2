"""CpSoftwareClusterCommunicationResourceProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 902)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class CpSoftwareClusterCommunicationResourceProps(ARObject, ABC):
    """AUTOSAR CpSoftwareClusterCommunicationResourceProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterCommunicationResourceProps."""
        super().__init__()


class CpSoftwareClusterCommunicationResourcePropsBuilder:
    """Builder for CpSoftwareClusterCommunicationResourceProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterCommunicationResourceProps = CpSoftwareClusterCommunicationResourceProps()

    def build(self) -> CpSoftwareClusterCommunicationResourceProps:
        """Build and return CpSoftwareClusterCommunicationResourceProps object.

        Returns:
            CpSoftwareClusterCommunicationResourceProps instance
        """
        # TODO: Add validation
        return self._obj
